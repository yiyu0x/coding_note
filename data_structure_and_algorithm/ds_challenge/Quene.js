function Queue() {

	let queue = [];

	this.push = function (value) {
		queue.push(value);
	}

	this.pop = function () {
		if ( queue.length==0 ) {
			console.log('Queue is Empty. Can\'t pop.');
			return;
		}
		queue.shift();
	}

	this.print = function () {
		return queue;
	}
}

var q = new Queue();
q.push(1)
q.push(2)
q.pop()
q.push(2)
console.log(q.print())