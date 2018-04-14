// 2017.12.24 edited
class Node{
	int data;
	Node next;
	Node(int data){
		this.data=data;
		this.next=null;
	}
}

public class CircleList{

	public static void printList(Node head,Node tail){
		Node tmp = head;
		do{
			System.out.print(tmp.data+" ");
			tmp = tmp.next;
			if(tmp==tail){
				System.out.print(tail.data+" ");
				break;
			}

		}while(tmp!=tail);
	}

	public static void catNode(Node node,Node head,Node tail){

		tail.next = node;
		node.next = head;
	}

	public static void main(String[] args) {
		
		Node head = new Node(1);
		Node tail = head;

		for(int i=2;i<=9;i++){
			Node tmp = new Node(i);
			catNode(tmp,head,tail);
			tail = tmp;
		}

		printList(head,tail);
	}


}