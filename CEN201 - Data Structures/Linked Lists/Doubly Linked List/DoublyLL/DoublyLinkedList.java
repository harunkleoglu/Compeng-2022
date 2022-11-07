public class DoublyLinkedList {
	
	Node head;
	
	public DoublyLinkedList() {
		this.head = null;
		this.head.next = null;
	}
	
	public Node zeroth() {
		return head;
	}
	
	public Node first() {
		return head.next;
	}
}

