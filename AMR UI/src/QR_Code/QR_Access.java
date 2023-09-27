package QR_Code;

import java.util.ArrayList;

public class QR_Access {
	
	private static ArrayList<QR_Object> QR_Codes;
	
	public static void initialize() {
		QR_Codes = new ArrayList<QR_Object>();
	}
	
	
	public static void loadQRCodes() {
		
	}
	
	public static void addQR(QR_Object qr) {
		if(qr == null) return;
		QR_Codes.add(qr);
	}
	
	public static ArrayList<QR_Object> getQRs() {
		ArrayList<QR_Object> list = new ArrayList<QR_Object>();
		for(int index = 0; index < QR_Codes.size(); index++) {
			list.add(QR_Codes.get(index));
		}
		return list;
	}
	
	public static QR_Object getQrByPosition(int x, int y) {
		
		// Search through all of QR list
		for(int index = 0; index < QR_Codes.size(); index++) {
			
			// If QR code has the same x and y position, return QR
			if(QR_Codes.get(index).getX_pos() == x && QR_Codes.get(index).getY_pos() == y) {
				return QR_Codes.get(index);
			}
		}
		return null;
	}
	
	public static QR_Object getQrByQRCode(String QRCode) {
		
		// Search through all of QR list
		for(int index = 0; index < QR_Codes.size(); index++) {
			
			// If QR has the same QR code, return QR
			if(QR_Codes.get(index).getQRCode().equals(QRCode)) {
				return QR_Codes.get(index);
			}
		}
		return null;
				
	}
	
	public static ArrayList<QR_Object> getNearbyQR(int x, int y){
		
		ArrayList<QR_Object> list = new ArrayList<QR_Object>();
		
		//search through all of QR list
		for(int index = 0; index < QR_Codes.size(); index++) {
			
			int x_pos = QR_Codes.get(index).getX_pos();
			int y_pos = QR_Codes.get(index).getY_pos();
			
			if(x_pos == x && y_pos == y) continue;
			
			// If x and y coordinates of QR are 1 away, add to list
			if(Math.abs(x_pos - x) <= 1 && Math.abs(y_pos - y) <= 1) {
				list.add(QR_Codes.get(index));
			}
		}

		
		return list;
	}
	
	
	
}
