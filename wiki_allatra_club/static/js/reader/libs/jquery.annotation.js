
jQuery.extend({
    annotation: function (node, re, nodeName, className, title, content) {
        if (node.nodeType === 3) {
            var match = node.data.match(re);
            if (match) {
                var annotation = document.createElement(nodeName || 'span');
                annotation.className = className || 'annotation';
                var wordNode = node.splitText(match.index);
                wordNode.splitText(match[0].length);
                var wordClone = wordNode.cloneNode(true);
                annotation.appendChild(wordClone);
                wordNode.parentNode.replaceChild(annotation, wordNode);
                                //console.log(wordNode);
                $(annotation).webuiPopover({
                    html: true,
                    trigger: 'click',
                    placement: 'left',
                    constrains: 'vertical',
                    arrow: false,
                    closeable: true,
                    //title: title,
                    content: content,
                    width:300,
                    height:200
                });
                //TODO: fix strange behavior
                return 1; //skip added node in parent
            }
        } else if ((node.nodeType === 1 && node.childNodes) && // only element nodes that have children
                !/(script|style)/i.test(node.tagName) && // ignore script and style nodes
                !(node.tagName === nodeName.toUpperCase() && node.className === className)) { // skip if already annotationed
            for (var i = 0; i < node.childNodes.length; i++) {
                i += jQuery.annotation(node.childNodes[i], re, nodeName, className, title, content);
            }
        }
        return 0;
    }
});

jQuery.fn.unannotation = function (options) {
    var settings = { className: 'annotation', element: 'span' };
    jQuery.extend(settings, options);

    return this.find(settings.element + "." + settings.className).each(function () {
        var parent = this.parentNode;
        parent.replaceChild(this.firstChild, this);
        parent.normalize();
    }).end();
};

jQuery.fn.annotation = function (words, options) {
    var settings = { className: 'annotation', element: 'span',
        caseSensitive: false, wordsOnly: false };
    jQuery.extend(settings, options);


    if (words.constructor === String) {
        words = [words];
    }
    words = jQuery.grep(words, function(word, i){
      return word != '';
    });
    words = jQuery.map(words, function(word, i) {
      return word.replace(/[-[\]{}()*+?.,\\^$|#\s]/g, "\\$&");
    });
    if (words.length == 0) { return this; };

    var flag = settings.caseSensitive ? "" : "i";
    var pattern = "(" + words.join("|") + ")";
    if (settings.wordsOnly) {
        pattern = "\\b" + pattern + "\\b";
    }
    var re = new RegExp(pattern, flag);

     //$.each(settings.text, function (index, row) {
     //
     //});
    return this.each(function () {
        jQuery.annotation(this, re, settings.element, settings.className, settings.title, settings.content);
    });
};

