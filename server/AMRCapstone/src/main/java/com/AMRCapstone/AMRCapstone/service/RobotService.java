package com.AMRCapstone.AMRCapstone.service;

import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

import com.AMRCapstone.AMRCapstone.Codes;
import com.AMRCapstone.AMRCapstone.access.QRAccess;
import com.AMRCapstone.AMRCapstone.access.QR_Queue;
import com.AMRCapstone.AMRCapstone.access.RobotAccess;
import com.AMRCapstone.AMRCapstone.model.QR;
import com.AMRCapstone.AMRCapstone.model.Robot;

@Service
public class RobotService {
    public Robot get() {
        Robot robot = RobotAccess.getRobot();
        if (robot == null) {
            RobotAccess.initialize();
            robot = RobotAccess.getRobot();
        }
        return robot;
    }

    public ResponseEntity<float[]> update(Robot temp) {
        Robot robot = RobotAccess.getRobot();
        if (robot == null) {
            RobotAccess.initialize();
            robot = RobotAccess.getRobot();
        }
        // validation
        // check status
        if (temp.getStatus().equals(Codes.statusActive) || temp.getStatus().equals(Codes.statusInactive)) {
            robot.setStatus(temp.getStatus());
        }
        // check message
        if (temp.getMessage().equals(Codes.FoundObjMessage) ||
                temp.getMessage().equals(Codes.FoundQRMessage) ||
                temp.getMessage().equals(Codes.HeadingMesssage) ||
                temp.getMessage().equals(Codes.NotConnectedMessage) ||
                temp.getMessage().equals(Codes.ScanningMessage) ||
                temp.getMessage().equals(Codes.UserControl)) {
            robot.setMessage(temp.getMessage());
        }
        if (temp.getMessage().equals(Codes.LostMessage)) {

            QR prev = QR_Queue.getPrevQR();
            QR_Queue.initialize();
            QR_Queue.addQR(prev);

            robot.setMessage(temp.getMessage());
        }

        // update robot
        robot.setX_pos(temp.getX_pos());
        robot.setY_pos(temp.getY_pos());
        robot.setRotation(temp.getRotation());

        robot.setQrScan(temp.getQrScan());
        robot.addtoLoggerList(temp.getLoggerList());
        robot.setImage(temp.getImage());

        HttpStatus status;

        if (robot.getQrScan() == null) {
            status = HttpStatus.OK;
        }
        // test QR Scan
        else {
            // check QRQueue
            if (QR_Queue.getCurrentQR().getCode().equals(robot.getQrScan())) {
                // pop queue
                QR_Queue.pop();
                QR_Queue.QueueUp();

                robot.setQrScan(null);
                status = HttpStatus.CONTINUE;

            } else if (QRAccess.getQrByQRCode(robot.getQrScan()) != null) {
                // reset Queue
                QR resetQR = QRAccess.getQrByQRCode(robot.getQrScan());
                if (resetQR == null) {
                    status = HttpStatus.CONFLICT;
                } else {
                    QR_Queue.resetQueue(resetQR);
                    QR_Queue.pop();
                    QR_Queue.QueueUp();
                    robot.setQrScan(null);
                    // send out destination, QR position, Http status I-am-a-tea-pot
                    status = HttpStatus.ACCEPTED;
                }

            } else {
                status = HttpStatus.NOT_FOUND;
            }

        }
        // //ensures
        // if (QR_Queue.getPrevQR() != null) {
        // while (QR_Queue.getCurrentQR().getX_pos() == QR_Queue.getPrevQR().getX_pos()
        // && QR_Queue.getCurrentQR().getY_pos() == QR_Queue.getPrevQR().getY_pos()) {
        // QR_Queue.pop();
        // QR_Queue.QueueUp();
        // }
        // }

        robot.setX_destination(QR_Queue.getCurrentQR().getX_pos());
        robot.setY_destination(QR_Queue.getCurrentQR().getY_pos());
        robot.setQrScan(null);

        float[] response;

        if (status.equals(HttpStatus.ACCEPTED) || status.equals(HttpStatus.CONTINUE)) {
            response = new float[4];

            // destination
            response[0] = robot.getX_destination();
            response[1] = robot.getY_destination();
            if (QR_Queue.getPrevQR() != null) {
                // QR position
                response[2] = QR_Queue.getPrevQR().getX_pos();
                response[3] = QR_Queue.getPrevQR().getY_pos();
            }

        }

        else {
            response = new float[2];
            response[0] = robot.getX_destination();
            response[1] = robot.getY_destination();

        }

        // create response

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        return new ResponseEntity<float[]>(response, headers, HttpStatus.OK);
    }

    public String getUserControl() {
        Robot robot = RobotAccess.getRobot();
        if (robot == null) {
            RobotAccess.initialize();
            robot = RobotAccess.getRobot();
        }
        return robot.getUserSignal();
    }
}
