package LinkedList;

public class LinkedList {
	Node head;

	public LinkedList() {
		head = null;
	}

	public boolean isEmpty() {
		if (head == null)
			return true;
		else
			return false;
	}

	public Node zeroth() {
		return head;
	}

	public Node first() {
		return head.next;
	}

	public void insertAfter(int data, Node eleman) {
		if (eleman != null) {
			// linked list boş değilse
			Node yeniEklenecek = new Node(data, eleman.next);
			eleman.next = yeniEklenecek;
		} else {
			// eğer linked list boşsa
			Node yeniEklenecek = new Node(data, head);
			head = yeniEklenecek;
		}
	}

	public Node find(int aranan) {
		Node gezici = first();

		while (gezici != null) {
			if (gezici.data == aranan) {
				return gezici;

			}

			else {
				gezici = gezici.next;
			}
		}
		return null;
	}

	public Node findPrevious(int data) {
		Node gezici = zeroth();

		while (gezici.next != null) {
			if (gezici.next.data == data) {
				return gezici;
			} else {
				gezici = gezici.next;
			}
		}

		return null;
	}

	public void remove(int data) {

		Node silinecek = find(data);
		Node onceki = findPrevious(data);
		if (onceki != null) {
			onceki.next = silinecek.next;
		}

	}

	public void printAll() {
		Node gezici = zeroth();

		while (gezici != null) {
			System.out.print(gezici.data + ",");
			gezici = gezici.next;
		}
	}

	/*
	 * public void insert(int data) { Node gezici=zeroth();
	 * 
	 * if(gezici==null) { Node yeniEklenecek=new Node(data,gezici.next); head =
	 * yeniEklenecek; } else { while(gezici.next!=null) { gezici=gezici.next; } Node
	 * yeniEklenecek=new Node(data,gezici.next); gezici.next = yeniEklenecek;
	 * yeniEklenecek = null; }
	 * 
	 * 
	 * }
	 */
}