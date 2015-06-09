EPUBJS.reader.annotation = {};


EPUBJS.reader.annotation.SERVER = window.location.origin;

EPUBJS.reader.annotation.request = function (book_id, chapterCfi, callback) {
    var fetch = $.ajax({
        dataType: "json",
        url: EPUBJS.reader.annotation.SERVER + "/api/annotation?book_id=" + book_id +
        "&chapter_cfi=" + encodeURIComponent(chapterCfi)
    });

    fetch.fail(function (err) {
        console.error(err);
    });

    fetch.done(function (results) {
        callback(results);
    });
};


//EPUBJS.reader.plugins.AnnotationController = function(Book) {
//   	var reader = this;
//    Book.
//};
EPUBJS.Hooks.register("beforeChapterDisplay").annotation = function (callback, renderer) {
    //console.log(renderer);
    var currentChapterCfi = renderer.currentChapterCfiBase; // "/6/14[xchapter_001]!"
    var book_id = window.location.pathname.match("[0-9]+");

    var s = document.createElement("style");
    s.innerHTML =".annotation { border-bottom: 2px dotted #800000; font-weight: normal; }";

    renderer.render.document.head.appendChild(s);

    EPUBJS.reader.annotation.request(book_id, currentChapterCfi, function (data) {
        var gotChapterCfi = data.chapterCfi;
        var gotHref = data.href;
        var gotResults = data;
        var iframeDoc;

        if(iframeDoc) {
                $(iframeDoc).find('body').unannotation();
            }
        var title;
        $.each(gotResults, function (index, row) {
            //console.log(row.words);
                content = '<div style="overflow-y: auto">';
                $.each(row.articles, function (index, article) {
                    //console.log(article)
                    var newContent =
                        '<div class="panel panel-default"> ' +
                            '<div class="panel-body" style="padding-top: 0;">' +
                                '<h3 style="margin-bottom: 0px;margin-top: 5px;">'+ article.title + '</h3>'+
                                '<hr style="margin-top: 5px; margin-bottom: 10px;">' +

                                article.content +' ' +
                            '</div>' +
                            '<div class="panel-footer"><a class="text-primary" target="_blank" href="' + article.url + '">'+ 'Читать дальше' + '</a>'+
                        '</div></div></div>';
                    content = content + newContent;
                });
            iframeDoc = $("#viewer iframe")[0].contentDocument;
            $(iframeDoc).find('body').annotation(row.words, {element: 'span', title: title,
                content: content});
        });
    });
    if (callback) callback();

};