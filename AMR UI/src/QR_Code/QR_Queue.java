package QR_Code;

import java.util.ArrayList;

public class QR_Queue {
	
	private static QR_Object prevQR = null;
	private static ArrayList<QR_Object> queue;
	protected static final int sizeOfQueue = 5;
	
	// initializes the array list and loads 5 queues into the queue list
	public static void initialize() {
		queue = new ArrayList<QR_Object>(sizeOfQueue);
	}
	
	protected static ArrayList<QR_Object> getQueue() {
		return queue;
	}
	
	
	// adds a qr code to the queue
	public static void addQR(QR_Object qr) {
		if(qr != null)
			queue.add(qr);
	}
	
	// adds a qr code to the front of the queue
	public static void addQRCurrent(QR_Object qr) {
		if(qr != null) {
			queue.clear();
			queue.add(0, qr);
			addToQueue();
		}
		
	}
	
	// gets the current qr code the robot is heading to
	public static QR_Object getCurrentQR() {
		if(queue.size() > 0)
			return queue.get(0);
		return null;
	}
	
	// gets the qr code the robot has just been at
	public static QR_Object getPrevQR() {
		return prevQR;
	}
	
	// removes the current qr code, moves it to the previous and brings the queue forward
	public static void pop() {
		if(queue.size() > 0) {
			QR_Object qr = queue.get(0);
			queue.remove(0);
			prevQR = qr;
		}
	}
	
	// fills the queue
	protected static void addToQueue() {
		while(queue.size() < sizeOfQueue && queue.size() > 0) {
			
			// gets the qr code last in the queue and gets its x and y position
			int lastXPos = queue.get(queue.size() - 1).getX_pos();
			int lastYPos = queue.get(queue.size() - 1).getY_pos();
//			System.out.println(QR_Access.getQrByPosition(lastXPos, lastYPos).getName());
			// gets the surrounding qr codes of the last qr code
			ArrayList<QR_Object> nearbyQR = QR_Access.getNearbyQR(lastXPos, lastYPos);
			
			// no nearby qr codes will result in an error
			if(nearbyQR.size() == 0) throw new IllegalStateException();
			
			// starts index at 0
			int index = 0;
			
			// if there is more than one nearby qr code
			if(nearbyQR.size() > 1) {
				
				// loop continuously
				while(true) {
//					System.out.println("nearby size: " + nearbyQR.size());
					// pick an index at random
					index = (int) (Math.random() * nearbyQR.size());
//					System.out.println("index: " + index);
//					System.out.println("Queue size: " + queue.size());
					//if queue has 2 or more qr codes, check if the last qr code has come from the one chosen form index
					if(queue.size() >= 2) {
//						System.out.println("second to last queue: " + queue.get(queue.size() - 2).getName());
						if( queue.get(queue.size() - 2) != nearbyQR.get(index)) {
//							System.out.println("breaking from loop");
							// break from loop
							break; 
						}
							
							
					}
					//only one qr code, no need to check if the last qr code has come from the one chosen form index
					else {
//						System.out.println("queue size is less than 2");
						break;
					}

				}
			}
			//add the chosen qr code
			addQR(nearbyQR.get(index));
		}
		// if there is nothing in the queue, pick a random qr code to add to the queue
		if(queue.size() == 0) {
			ArrayList<QR_Object> list = QR_Access.getQRs();
			int index = (int) ((Math.random() * 1000) % list.size());
			queue.add(list.get(index));
			addToQueue();
		}
	}
	
	
	
	// finds out whether a qr code is in the queue or not
	public static boolean isInQueue(QR_Object qr) {
		
		for(int index = 0; index < queue.size(); index++) {
			if(queue.get(index).equals(qr)) return true;
		}
		
		return false;
	}
	

}
