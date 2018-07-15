function Stack() {

	let Stack = [];

	this.push = function (value) {
		Stack.push(value);
	}

	this.pop = function () {
		if ( Stack.length==0 ) {
			console.log('Stack is Empty. Can\'t pop.');
			return;
		}
		Stack.pop();
	}

	this.print = function () {
		return Stack;
	}
}

var s = new Stack();
s.push(1)
s.push(2)
s.pop()
s.push(3)
console.log(s.print())