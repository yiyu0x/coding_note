function BinarySearchTree () {
	
	let head = null;
	const Node = function (value) {
		this.value = value;
		this.left = null;
		this.right = null;
	}

	this.add = function (value,current=head) {
		let node = new Node(value);
		if ( !head ) {
			head = node;
		} else {
			let left = current.left;
			let right = current.right;

			if ( value <= current.value ) {
				if ( !left ) {
					current.left = node;
				} else {
					this.add( value, left);
				}
			} else if ( value > current.value ) {
				if ( !right ) {
					current.right = node;
				} else {
					this.add( value, right);
				}
			}
		}
	}

	this.find = function (value ,current=head) {

		while ( current ) {
			
			if ( current.value==value ) {
				return true;
			}

			if ( value>current.value ) {
				return this.find( value,current.right );
			} else {
				return this.find( value,current.left );
			}
		}
		return false
	}
	this.traversal_inorder = function (current=head) {
		if ( current ) {
			this.traversal_inorder(current.left)
			console.log(current.value);
			this.traversal_inorder(current.right)
		} 
	}

	this.traversal_preorder = function (current=head) {
		if ( current ) {
			console.log(current.value);
			this.traversal_inorder(current.left)
			this.traversal_inorder(current.right)
		} 
	}

	this.traversal_postorder = function (current=head) {
		if ( current ) {
			this.traversal_inorder(current.left)
			this.traversal_inorder(current.right)
			console.log(current.value);
		} 
	}
 
}
var b = new BinarySearchTree();
for (let i=0;i<25;i++) {
	let ran = Math.floor( Math.random()*50 + 1 );
	b.add(ran);
}

b.traversal_inorder()
