function LinkList () {

	let head = null;
	const Node = function (value) {
		this.value = value;
		this.next = null;
	}

	this.append = function (value) {
		let node = new Node(value);
		if ( head==null) {
			head = node;
		} else {
			
			let current = head;
			while ( current ) {
				if ( current.next == null ) {
					current.next = node;
				}
				current = current.next;
			}
		}
	}

	this.delete = function (value) {
		if ( head.value = value ) {
			head = head.next;
		} else {
			let current = head;
			while ( current ) {
				if ( current.next.value == value) {
					current.next = current.next.next;
				}
				current = current.next;
			}
		}
	}

	this.print = function () {
		if ( head!= null) {
			let current = head;
			while ( current ) {
				console.log(current.value);
				current = current.next;
			}
		}
	}
}

function HashTable () {

	let hashTable = []
	this.hashKey = function (value) {
		let hash = 0;
		for ( let i=0;i<value.length;i++ ) {
			hash += value.charCodeAt(i);
		}

		return hash%10;
	}

	this.append = function (value) {
		let key = this.hashKey(value);
		if ( hashTable[key]==null ) {
			hashTable[key] = new LinkList();
		}

		hashTable[key].append(value);
	}

	this.delete = function (value) {
		let key = this.hashKey(value);
		if ( hashTable[key]==null ) {
			console.log('value not in hashtable. Can\'t delete');
			return;
		}

		hashTable[key].delete(value);
	}


	this.print = function () {
		for (let i=0;i<hashTable.length;i++ ) {
			if ( hashTable[i]!=null ) {
				console.log('key: ',i);		
				hashTable[i].print();	
			}
		}
	}
}

var h = new HashTable()
h.append('hello')
h.append('world')
h.append('javascript')
h.delete('hello')
h.append('javascript')
h.delete('javascript')
h.print()