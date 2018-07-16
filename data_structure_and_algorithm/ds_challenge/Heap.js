function Heap () {
	
	let head = null;
	const Node = function (value) {
		this.value = value;
		this.left = null;
		this.right = null;
	}

	this.add = function (value) {
		let node = new Node(value);
		if ( !head ) {
			head = node;
		} else {

			let current = head;
			
			while ( current ) {
				
				if ( !current.left ) {
					current.left = node;
				} 
				else if ( !current.right ) {
					current.right = node;
				}
			}

		}
	}


}
var h = new Heap();
for (let i=0;i<50;i++) {
	let ran = Math.floor( Math.random()*50 + 1 );
	h.add(ran);
}
