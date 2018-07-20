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
			if ( current.left ) {
				if ( current.left.value == target ) return current;	
				if ( this.findParent(target, current.left) ) { 
					return this.findParent(target, current.left);
				}
				
			}

			if ( current.right ) {
				if ( current.right.value == target ) return current;
				if ( this.findParent(target, current.right) ) {
					return this.findParent(target, current.right);
				}
			}

			return false;
		}

	}

	this.recolor = function (current) {
		// console.log(current.value)
		let father = this.findParent(current.value);
		// console.log(father.value)
		let grandfather = this.findParent( this.findParent(current.value).value );
		// console.log(grandfather.value)
		let uncle = null;
		if ( grandfather.left && grandfather.right ) {
			uncle = (grandfather.left==father) ? grandfather.right:grandfather.left;
		}
		// console.log(uncle.value)
		if ( father ) {
			father.color = 'black';
			if ( uncle ) {
				uncle.color = 'black';
			}
			if ( grandfather != this.head ) {
				grandfather.color = 'red';
			}
		}
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
				if ( current.color == 'red' ) this.recolor(node);
				return;
			} else if ( !current.right && node.value > current.value ) {
				current.right = node;
				if ( current.color == 'red' ) this.recolor(node);
				return;
			} 
			if ( node.value <= current.value) this.insert( node, current.left );
			else this.insert( node, current.right );

		}


	}
}

var r = new RBT();
r.insert(new Node(20));
r.insert(new Node(14));
r.insert(new Node(23));
r.insert(new Node(13));
// console.log(r.head);
console.log(r.head);