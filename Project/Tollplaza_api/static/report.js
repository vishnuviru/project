


var doc = new jsPDF('p','pt','a4');

doc.setFontSize(1);
doc.setLineWidth(1);

var specialElementHandlers = {
    '#editor': function (element, renderer) {
        return true;
    }
};

$('#cmd').click(function () {
    
    doc.fromHTML($('#container').html(), 10, 10, {
        'width': 1800,
            'elementHandlers': specialElementHandlers
    });
    doc.save('project.pdf');
});