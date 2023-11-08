package com.AMRCapstone.AMRCapstone.access;

import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

import com.AMRCapstone.AMRCapstone.model.QR;

public class QRAccess {
    // private static ArrayList<QR> QR_Codes;

    private static Map<String, QR> QRList;

    private final static String fileName = "QR_Data.txt";
    private final static String splitChar = "#";

    private static BufferedReader bufferedReader = null;

    public static void initialize() {
        // QR_Codes = new ArrayList<QR>();
        QRList = new HashMap<String, QR>();

        // loadQRCodes();
    }

    public static void loadQRCodes() {
        try {
            // directory to current file, /../../ returns two directories which is where
            // Create a FileReader and bufferedReader to read the file
            File file = new File(fileName);
            if (!file.exists()) {
                System.out.println("file does not exist at: " + file.getAbsolutePath());
                System.out.println(file.getCanonicalPath());
                return;
            }
            FileReader fileReader = new FileReader(file);
            bufferedReader = new BufferedReader(fileReader);

            String line;
            int count = 0;

            // Reads each line in data file
            while ((line = bufferedReader.readLine()) != null) {
                System.out.println("another QR code");
                // Prints line for testing
                System.out.println(line);

                // Splits data into tokens
                String[] qrData = line.split(splitChar);

                // Ensures correct number of tokens
                if (qrData.length != 5)
                    throw new Exception("data is corrupted");

                // Initializes data to objects
                // String fileName = qrData[0]; /* --- NOT NEEDED - FOR REFERENCE WHEN LOOKING
                // INTO FILE--- */
                String qrCode = qrData[1];
                int x_pos = Integer.parseInt(qrData[2]);
                int y_pos = Integer.parseInt(qrData[3]);
                String status = qrData[4];

                // Creates and adds qr object to access list
                QR temp = new QR(status, qrCode, x_pos, y_pos);
                addQR(temp);
                count++;
                System.out.println(count);

            }

            // Close BufferedReader
            // bufferedReader.close();

        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            if (bufferedReader != null)
                try {
                    bufferedReader.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }

        }

    }

    public static void saveQRCodes() {
        System.out.println("Saving QR Codes");

        try {
            File file = new File(fileName);
            if (!file.exists()) {
                file.createNewFile();
            } else {
                file.delete();
                file.createNewFile();
            }

            FileWriter myWriter = new FileWriter(fileName);
            for (QR q : QRList.values()) {
                myWriter.append(q.toString() + "\n");
            }
            myWriter.close();
            System.out.println("Successfully wrote to the file.");
        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
        System.out.println("Finished Saving QR Codes");
    }

    public static void addQR(QR qr) {
        if (qr == null)
            return;
        // QR_Codes.add(qr);
        QRList.put(qr.getName(), qr);
        /* --- SHOULD BE COMMENTED OUT FOR TEST CASES --- */
        saveQRCodes();
    }

    public static Map<String, QR> getQRs() {
        return QRList;
    }

    public static QR getQrByPosition(float x, float y) {

        for (QR qr : QRList.values()) {
            if (qr.getX_pos() == x && qr.getY_pos() == y) {
                return qr;
            }
        }

        return null;
    }

    public static QR getQrByQRCode(String QRCode) {

        for (QR qr : QRList.values()) {
            if (qr.getCode().equals(QRCode)) {
                return qr;
            }
        }

        return null;

    }

    public static ArrayList<QR> getNearbyQR(float x, float y) {

        ArrayList<QR> list = new ArrayList<QR>();

        for (QR qr : QRList.values()) {
            float x_pos = qr.getX_pos();
            float y_pos = qr.getY_pos();

            if (x_pos == x && y_pos == y)
                continue;

            // If x and y coordinates of QR are 1 away, add to list
            else if (Math.abs(x_pos - x) <= 1 && Math.abs(y_pos - y) <= 1) {
                list.add(qr);
            }
        }

        return list;
    }

}
