var width = 1000;
var height = 650;
var duration = 3000;

var customBase = document.createElement('custom');
var custom = d3.select(customBase); 

var chart = d3.select('canvas')
              .attr("class", "layer")
              .attr("width", width)
              .attr("height", height)
var context = chart.node().getContext('2d');

function create_points(dataset) {
  var join = custom.selectAll('custom.rect')
                   .data(dataset);
  
  var enterSel = join.enter()
                     .append("custom")
                     .attr('class', 'rect')
                     .classed("arc", true)
                     .attr("x", function(d) {return d.ending_x_position})
                     .attr("y", function(d) {return d.ending_y_position})
                     .attr("radius", function(d) {return d.radius})
                     .attr("fillStyle", function(d) {return d.color})

  join.merge(enterSel)
      .transition()
      .duration(duration)
      .attr("x", function(d) {return d.line_x_position})
      .attr("y", function(d) {return d.line_y_position})

  var exitSel = join.exit()
                    .remove();
   drawCanvas();
}

function drawCanvas() {
  context.clearRect(0, 0, width, height); 
  var elements = custom.selectAll('custom.rect');
    elements.each(function(d) {
    var node = d3.select(this);
    context.beginPath();
    context.arc(node.attr("x"), node.attr("y"), node.attr("radius"), 0, 2 * Math.PI);
    context.fillStyle = node.attr("fillStyle");
    context.stroke();
    context.strokeStyle = "#D3D3D3";
    context.lineWidth = 1;
    context.fill();
    context.closePath();
  })
}

make_base();

d3.csv("data/other_school_line_data.csv", function(error, dataset) { create_points(dataset) });





d3.select('body').append('div')
  .attr('class', 'play-control')
  .on('click', function () {
    var t = d3.timer(function(elapsed) {
      drawCanvas();
      if (elapsed > duration) t.stop();
    })
  });


