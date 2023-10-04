package QR_Code;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class QR_Access {
	
	private static ArrayList<QR_Object> QR_Codes;
	private final static String fileName = "/QR_Data.txt";
	
	public static void initialize() {
		QR_Codes = new ArrayList<QR_Object>();
	}
	
	
	public static void loadQRCodes() {
		try {
			// directory to current file, /../../ returns two directories which is where file is located
			String filePath = new File("").getAbsolutePath() + fileName;
			// Create a FileReader and bufferedReader to read the file
			FileReader fileReader = new FileReader(filePath);
			BufferedReader bufferedReader = new BufferedReader(fileReader);

			String line;
			int count = 0;

			// Reads each line in data file
			while ((line = bufferedReader.readLine()) != null) {
				// Prints line for testing
				System.out.println(line);
				
				// Splits data into tokens
				String[] qrData = line.split("#");
				
				// Ensures correct number of tokens
				if(qrData.length != 5) throw new Exception("data is corrupted");
				
				// Initializes data to objects
				String fileName = qrData[0];
				String qrCode = qrData[1];
				int x_pos = Integer.parseInt(qrData[2]);
				int y_pos = Integer.parseInt(qrData[3]);
				String status = qrData[4];
				
				// Creates and adds qr object to access list
				QR_Object temp = new QR_Object(fileName, qrCode, x_pos, y_pos, status);
				addQR(temp);
				count++;
				System.out.println(count);
				
			}

			// Close BufferedReader
			bufferedReader.close();
		} catch (Exception e) {
			e.printStackTrace();
		}	

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
