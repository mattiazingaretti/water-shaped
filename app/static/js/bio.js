
// Make an instance of two and place it on the page.
var d = document.getElementById('d-start');

var params = { width: 285, height: 200 };
var two = new Two(params).appendTo(d);


// two has convenience methods to create shapes.
var circle = two.makeCircle(100, 100, 10);
var rect = two.makeRectangle(213, 100, 100, 100);
var path = two.makePath(100, 100, 100 , 150);
var text = new  Two.Text("Test", 0 , 0  );

text.visible = true;

// The object returned has many stylable properties:
circle.fill = '#FF8000';
circle.stroke = 'orangered'; // Accepts all valid css color
circle.linewidth = 3;

rect.fill = 'rgb(0, 200, 255)';
rect.opacity = 0.75;
rect.noStroke();

// Don't forget to tell two to render everything
// to the screen
two.update();

