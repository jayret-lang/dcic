jQuery(document).ready(function($) {
  function extractMarks(text) {
    var lines = text.split(/\r\n?|\n/);
    var marks = {byLine: [], byNum: Object.create(null)};
    var count = 0;
    for (var lineNo = 0; lineNo < lines.length; lineNo++) {
      marks.byLine[lineNo] = [];
      var idx = undefined;
      while ((idx = lines[lineNo].search(/~hl:([a-z/]+:)?\d+:[se]~/)) >= 0) {
        var m = lines[lineNo].match(/~hl:([a-z/]+:)?(\d+):([se])~/);
        var match = m[0];
        var style;
        var num = m[2];
        if (!m[1]) {
          style = "hilite-" + num;
        } else {
          style = m[1].substring(0, m[1].length - 1);
        }
        var openClose = m[3];
        lines[lineNo] = lines[lineNo].replace(match, "");
        if (openClose === "s") {
          count++;
          marks.byNum[num] = {startLine: lineNo, startCol: idx, number: num, style: style};
          if (marks.byLine[lineNo][idx] === undefined)
            marks.byLine[lineNo][idx] = {open: [], close: []};
          marks.byLine[lineNo][idx].open.push(marks.byNum[num]);
        }
        else if (marks.byNum[num] !== undefined) {
          marks.byNum[num].endCol = idx;
          marks.byNum[num].endLine = lineNo;
          if (marks.byLine[lineNo][idx] === undefined)
            marks.byLine[lineNo][idx] = {open: [], close: []};
          marks.byLine[lineNo][idx].close.unshift(marks.byNum[num]);
        } else {
          console.error("No information found for mark " + JSON.stringify(m));
        }
      }
    }
    return {count: count, text: lines.join("\n"), marks: marks};
  }

  function applyMarks(code, allMarks) {
    var curCol = 0;
    var curLine = 0;
    var openMarks = " ";
    var curReplacement = undefined;
    function updateMarks(marks) {
      if (marks) {
        marks.close.forEach(function(m) {
          openMarks = openMarks.replace(m.style + " ", "");
          if (m.element && m.element === curReplacement) {
            curReplacement = undefined;
          }
        });
        marks.open.forEach(function(m) {
          if (openMarks.search(m.style) == -1) { openMarks = m.style + " " + openMarks; }
          if (m.element && curReplacement === undefined) {
            curReplacement = m.element;
          }
        });
      }
    }
    function wrapMarks(node) {
      openMarks.trim().split(" ").forEach(function(m) {
        node = $("<span>").addClass(m.replace(/\//g, " ")).addClass("hilite").append(node);
      });
      if (curReplacement) {
        node.appendTo(curReplacement.inner);
        return $(curReplacement.outer);
      }
      return node;
    }
    var childNodes = Array.from(code.childNodes);
    for (var i = 0; i < childNodes.length; i++) {
      var marks = allMarks.byLine[curLine] || [];
      if (curCol === 0) {
        updateMarks(marks[0]);
      }
      var kid = childNodes[i];
      if (kid.nodeType === 3 && kid.textContent === "\n") {
        curCol = 0;
        curLine++;
      } else {
        var newEnd = curCol + kid.textContent.length;
        var c = curCol + 1;
        for (; c < newEnd; c++) {
          if (marks[c] !== undefined && (marks[c].open.length > 0 || marks[c].close.length > 0)) {
            var newKid1 = wrapMarks($("<span>").attr("class", $(kid).attr("class"))
                                               .text($(kid).text().substring(0, c - curCol)));
            updateMarks(marks[c]);
            var newKid2 = wrapMarks($("<span>").attr("class", $(kid).attr("class"))
                                               .text($(kid).text().substring(c - curCol)));
            $(kid).replaceWith(newKid1);
            newKid1.after(newKid2);
            curCol = c;
            break;
          }
        }
        if (c == newEnd) {
          if (openMarks !== " ") {
            var newKid = wrapMarks($("<span>").text($(kid).text())
                                              .attr("class", $(kid).attr("class")))[0];
            code.replaceChild(newKid, kid);
          }
          curCol = newEnd;
        }
        updateMarks(marks[curCol]);
      }
    }
  }

  $("code.sourceCode").each(function(_, code) {
    if ($(code).data("lang")) {
      var counter = Date.now();
      var $heaprefs = $(code).children(".heapref");
      var markElts = Object.create(null);
      if ($heaprefs.length > 0) {
        $heaprefs.each(function(_, span) {
          var outer = span;
          var inner = span;
          markElts[counter] = { outer: outer, inner: inner };
          while (inner.childElementCount === 1) {
            inner = inner.firstElementChild;
          }
          markElts[counter].inner = inner;
          var content = $(inner).text();
          outer.replaceWith("~hl:replace:" + counter + ":s~" + content + "~hl:" + counter + ":e~");
          $(inner).empty();
          counter++;
        });
      }
      var markedText = extractMarks($(code).text());
      for (let id in markElts) {
        markedText.marks.byNum[id].element = markElts[id];
      }
      CodeMirror.runMode(markedText.text, $(code).data("lang"), code);
      if (markedText.count > 0) applyMarks(code, markedText.marks);
      $(code).addClass("cm-s-default");
    }
  });
});
