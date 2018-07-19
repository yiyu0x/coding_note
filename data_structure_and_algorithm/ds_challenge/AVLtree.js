function AVLtree () {

	this.head = null;
	const Node = function (value) {
		this.value = value;
		this.left = null;
		this.right = null;
	}
	this.findParent = function (node,current=this.head) {
		while ( current ) {
			if ( current.left==node || current.right==node ) {
				// console.log('great')
				return current;
			}

			if ( current.right ) {
				return this.find( current.right )
			}

			if ( current.left ) {
				return this.find( current.right )
			}

			return
		}
	}

	this.LL = function ( pivot ) {
		//siple type
		if ( !pivot.right ) {
			let tmp = new Node(pivot.value);
			tmp.left = null;
			let pivot_next = pivot.left;
			//connect
			if ( pivot==this.head ) {
				this.head = pivot_next;
				pivot_next.right = tmp;
			} else {
				this.find(pivot.value).parent.left = pivot_next;
				pivot_next.right = tmp;
			}

		//complex type
		} else {	

			let pivot_next = pivot.right;
			let tmp = pivot_next.left;


			pivot_next.left = pivot;
			pivot.right = tmp;

			if ( pivot==this.head ) {
				this.head = pivot_next;
			} else {
				this.find(pivot.value).parent.right = pivot_next;
			}
		}
	}
	this.RR = function ( pivot) {
		//siple type
		if ( !pivot.left ) {
			let tmp = new Node(pivot.value);
			tmp.right = null;
			let pivot_next = pivot.right;
			//connect
			if ( pivot==this.head ) {
				this.head = pivot_next;
				pivot_next.left = tmp;
			} else {
				this.find(pivot.value).parent.right = pivot_next;
				pivot_next.left = tmp;
			}

		//complex type
		} else {

			let pivot_next = pivot.left;
			let tmp = pivot_next.right;

			pivot_next.right = pivot;
			pivot.left = tmp;

			//connect
			if ( pivot==this.head ) {
				this.head = pivot_next;
			} else {
				this.find(pivot.value).parent.left = pivot_next;
			}
		}
	}


	this.switchType = function () {
		let flag;
		// case table
		// LL :1
		// LR :2
		// RR :3
		// RL :4
		let target = this.findNodeNeedToBalance();
		if ( this.balanceFactor( target ) > 1 ) {
			flag = ( this.balanceFactor( target.left ) >= 0 )?1:2
		} else if ( this.balanceFactor( target ) < -1 ) {
			flag = ( this.balanceFactor( target.right ) <= 0 )?3:4
		}
		// console.log( flag );
		return flag;
	}
	this.balanceTree = function () {
		let node = this.findNodeNeedToBalance();
		// console.log('nedd to balance',node.value)
		switch ( this.switchType() ) {
			//LL
			case 1:
				this.LL(node);
				break;
			case 2:
				break;
			//RR
			case 3:
				this.RR(node);
				break;
		}

	}

	this.findNodeNeedToBalance = function (current=this.head,parent=this.head) {
		// console.log('debug---> bf',this.balanceFactor(current))
		// console.log('debug--->',current.value)
		while ( current ) {
			if ( this.balanceFactor(current) < -1 ||
				 this.balanceFactor(current) > 1 ) {
				//if bf greater then 1 , left tree is deeper than right tree
				//so must adjust left tree
				if ( this.balanceFactor(current) > 1 ) {
					parent = current;
					current = current.left;
				} else if ( this.balanceFactor(current) < -1 ) {
					parent = current;
					current = current.right;
				}
			} else {
				return parent;
			}
		}

		// return parent;
	}

	this.balanceFactor = function (current) {
		if ( current ) {
			let bf = this.height(current.left) - this.height(current.right)
			return bf;
		}
	}

	this.height = function (current) {
		if ( current ) {
			if ( !current.left && !current.right ) {
            	return 1;
            } else {
            	return 1 + ( this.height(current.left) > this.height(current.right) ?
            				this.height(current.left) : this.height(current.right));
            }
		}

		return 0;
	}


	this.add = function (value,current=this.head) {
		let node = new Node(value);
		if ( !this.head ) {
			this.head = node;
		} else {
			let left = current.left;
			let right = current.right;

			if ( value <= current.value ) {
				if ( !left ) {
					current.left = node;
					this.balanceTree()
				} else {
					this.add( value, left);
				}
			} else if ( value > current.value ) {
				if ( !right ) {
					current.right = node;
					this.balanceTree()
				} else {
					this.add( value, right);
				}
			}
		}
	}

	this.find = function (value ,current=this.head, parent=null) {

		while ( current ) {

			if ( current.value==value ) {
				return {current,parent};
			}

			if ( value>current.value ) {
				return this.find( value,current.right,current );
			} else {
				return this.find( value,current.left,current );
			}
		}
		return false
	}

	this.deleteHead = function (head=this.head) {

		if ( !head.left && !head.right ) {
			head = null;
		}
		//only have left leaf
		else if ( head.left && !head.right ) {
			head = head.left;
		}
		//only have right leaf
		else if ( !head.left && head.right ) {
			head = head.right;
		}
		//have two leafs
		else if ( head.left && head.right ) {
			this.adjust(head, head.left);
		}

	}

	// after delete leaf , adjust tree
	this.adjust = function (target, current, current_parent) {
		//find max on leaf || min on right
		if ( !current.right ) {
			target.value = current.value;
			current_parent.right = null;
			return;
		}
		return this.adjust(target, current.right, current);
	}

	this.delete = function (value) {

		if ( this.find(value) ) {

			if ( value==this.head.value ) {
				this.deleteHead();
				return
			}

			let target = this.find(value).current;
			let parent = this.find(value).parent;
			// console.log(parent.value)
			// console.log(target.value)
			let leafOnRight = (target.value>parent.value)?true:false;
			//not have any leaf

			if ( !target.left && !target.right ) {
				if ( leafOnRight ) {
					parent.right = null;
				} else {
					parent.left = null;
				}
			}
			//only have left leaf
			else if ( target.left && !target.right ) {
				if ( leafOnRight ) {
					parent.right = target.left;
				} else {
					parent.left = target.leftl;
				}
			}
			//only have right leaf
			else if ( !target.left && target.right ) {
				if ( leafOnRight ) {
					parent.right = target.right;
				} else {
					parent.left = target.right;
				}
			}
			//have two leafs
			else if ( target.left && target.right ) {
				//find max on leaf || min on right
				if ( !target.left.right ) {
					target.value = target.left.value;
					target.left = null;
				} else {
					this.adjust(target.left,target.left)
				}
			}
		}

	}
	this.traversal_inorder = function (current=this.head) {
		if ( current ) {
			this.traversal_inorder(current.left)
			console.log(current.value);
			this.traversal_inorder(current.right)
		}
	}

	this.traversal_preorder = function (current=this.head) {
		if ( current ) {
			console.log(current.value);
			this.traversal_inorder(current.left)
			this.traversal_inorder(current.right)
		}
	}

	this.traversal_postorder = function (current=this.head) {
		if ( current ) {
			this.traversal_inorder(current.left)
			this.traversal_inorder(current.right)
			console.log(current.value);
		}
	}



}
var b = new AVLtree();
// for (let i=0;i<25;i++) {
	// let ran = Math.floor( Math.random()*50 + 1 );
	// b.add(70);
	// b.add(50);
	// b.add(40);
	// b.add(60);
	// b.add(30);
	// b.add(45);
	// b.add(20);
	b.add(3);
	b.add(2);
	b.add(1);

// }
// b.traversal_inorder()
// console.log(b.balanceFactor(b.find(20).current))
// console.log(b)
// console.log(b.findNodeNeedToBalance().value)
// console.log(b.height(b.find(26).current))
b.traversal_inorder()
// console.log(b.findParent(b.find(40).current))
// console.log(b.find(40).parent)
console.log(b.head)