package LinkedList;

public class Main {
	public static void main(String[] args) {

		SinglyLinkedList senalinked = new LinkedList();

		senalinked.insert(6);
		senalinked.insert(7);
		senalinked.insert(68);

		System.out.println(senalinked.zeroth().data);
		senalinked.printAll();
	}
}
