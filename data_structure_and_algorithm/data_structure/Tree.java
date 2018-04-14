// 2017.12.24 edited
class Node{
	int data;
	Node left;
	Node right;
	Node(int data){
		this.data = data;
	}
}

public class Tree{
	
	static Node root;

	public static void showTree(Node tmp){

		if(tmp!=null){
			showTree(tmp.left);
			System.out.print(tmp.data+" ");	
			showTree(tmp.right);
		}
	}

	public static void addNode(Node now,Node tmp){

		if(now.data > tmp.data){
			if(tmp.right==null)
				tmp.right = now;
			else
				addNode(now,tmp.right);
		}else if(now.data <= tmp.data){
			if(tmp.left==null)
				tmp.left = now;
			else
				addNode(now,tmp.left);
		}
	}
// System.out.println("im "+now.data+"  small then "+tmp.data);
	public static void main(String[] args) {
		
		int []array = {2,7,4,9,4,2,5,8,3,5};

		for(int i=0;i<array.length;i++){
			if(i==0){
				root = new Node(array[0]);
				continue;
			}
			addNode(new Node(array[i]),root);
		}

		showTree(root);
	}
}
