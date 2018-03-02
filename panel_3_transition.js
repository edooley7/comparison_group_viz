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
                     .attr("x", function(d) {return d.starting_x_position})
                     .attr("y", function(d) {return d.starting_y_position})
                     .attr("radius", function(d) {return d.radius})
                     .attr("fillStyle", function(d) {return d.color})

  join.merge(enterSel)
      .transition()
      .duration(duration)
      .attr("x", function(d) {return d.ending_x_position})
      .attr("y", function(d) {return d.ending_y_position})

  var exitSel = join.exit()
                    .transition()
                    .attr("x", function(d) {return d.starting_x_position})
                    .attr("y", function(d) {return d.starting_y_position})
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
    context.fill();
    context.closePath();
  })
}

function make_base(left_position, right_position, width, height) {
  base_image = new Image();
  base_image.src = 'img/school_image_no_background.png';
  base_image.onload = function(){
    // left, top, width, height
    context.drawImage(base_image, left_position, right_position, width, height);
  }
}

make_base(-50, 120, 200, 300);

d3.csv("data/other_school_data.csv", function(error, dataset) { create_points(dataset) });

d3.select('body').append('div')
  .attr('class', 'play-control')
  .on('click', function () {
    var t = d3.timer(function(elapsed) {
      drawCanvas();
      if (elapsed > duration) t.stop();
    })
  });
