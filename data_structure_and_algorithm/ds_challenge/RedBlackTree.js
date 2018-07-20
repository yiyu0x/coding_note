const Node = function (value) {
	this.value = value;
	this.color = 'red';
	this.left = null;
	this.right = null;
}
function RBT () {

	this.head = null;

	this.findParent = function (target,current=this.head) {

		if ( current ) {
			if ( current.left==target ) return current;
			else if ( current.right==target ) return current;
			return this.findParent(target, current.left);
			return this.findParent(target, current.right);
		}

	}

	this.recolor = function (current) {
		this.findParent(current);
	}

	this.insert = function (node,current=this.head) {
		
		if ( !this.head ) {
			this.head = node;
			this.head.color = 'black';
			return;
		}

		if ( current ) {
			if ( !current.left && node.value <= current.value ) {
				current.left = node;
				return;
			} else if ( !current.right && node.value > current.value ) {
				current.right = node;
				return;
			}

			this.insert( node, current.left );
			this.insert( node, current.right );
		}


	}
}

var r = new RBT();
r.insert(new Node(20));
r.insert(new Node(22));
r.insert(new Node(26));
r.insert(new Node(15));
// console.log(r.head);
conosle.log(r.findParent(26));