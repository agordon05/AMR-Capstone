package com.AMRCapstone.AMRCapstone.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.AMRCapstone.AMRCapstone.model.Robot;
import com.AMRCapstone.AMRCapstone.service.RobotService;

import jakarta.validation.Valid;

@RestController
public class RobotController {
    // private Robot robot = new Robot(0, "Active", "Heading to QR code", 0, 0, 35,
    // 1, 1, null, new ArrayList<String>(),
    // "image");

    private final RobotService robotService;

    public RobotController(RobotService robotService) {
        this.robotService = robotService;
    }

    @GetMapping("/robot")
    public Robot getRobot() {
        return robotService.get();
    }

    @PutMapping("/robot")
    public ResponseEntity<float[]> updateRobot(@RequestBody Robot robot) {
        return robotService.update(robot);
    }

    @GetMapping("/robot/user")
    public String getUserControl() {
        return robotService.getUserControl();
    }
    // @GetMapping("/robot/status")
    // public String getStatus() {
    // return "Active";
    // }

    // @PutMapping("/robot/status")
    // public void updateStatus(@RequestBody @Valid String status) {
    // if (status == null)
    // throw new ResponseStatusException(HttpStatus.BAD_REQUEST);
    // RobotAccess.getRobot().setStatus(status);
    // }

    // @GetMapping("/robot/message")
    // public String getMessage() {
    // return "Heading to QR code";
    // }

    // @PutMapping("/robot/message")
    // public void updateMessage(@RequestBody @Valid String message) {
    // if (message == null)
    // throw new ResponseStatusException(HttpStatus.BAD_REQUEST);
    // RobotAccess.getRobot().setMessage(message);
    // }

    // @GetMapping("/robot/position")
    // public float[] getPostition() {
    // float[] position = {
    // RobotAccess.getRobot().getX_pos(),
    // RobotAccess.getRobot().getY_pos(),
    // RobotAccess.getRobot().getRotation()
    // };
    // return position;
    // }

    // @PutMapping("/robot/position")
    // public void updateposition(@RequestBody float x_pos, @RequestBody float
    // y_pos, @RequestBody float rotation) {
    // // if(message == null) throw new
    // // ResponseStatusException(HttpStatus.BAD_REQUEST);
    // RobotAccess.getRobot().setX_pos(x_pos);
    // RobotAccess.getRobot().setY_pos(y_pos);
    // RobotAccess.getRobot().setRotation(rotation);
    // }

    // @GetMapping("/robot/destination")
    // public float[] getDestination() {
    // float[] destination = {
    // RobotAccess.getRobot().getX_destination(),
    // RobotAccess.getRobot().getY_destination()
    // };
    // return destination;
    // }

    // @PutMapping("/robot/destination")
    // public void setDestination(@RequestBody float x_pos, @RequestBody float
    // y_pos) {
    // RobotAccess.getRobot().setX_destination(x_pos);
    // RobotAccess.getRobot().setY_destination(y_pos);
    // }

    // @GetMapping("/robot/qr")
    // public String getQRScan() {
    // return RobotAccess.getRobot().getQrScan();
    // }

    // @PutMapping("/robot/qr")
    // public void SetQRScan(@RequestBody String code) {
    // if (code == null)
    // throw new ResponseStatusException(HttpStatus.BAD_REQUEST);
    // RobotAccess.getRobot().setQrScan(code);
    // }

    // @GetMapping("/robot/log")
    // public ArrayList<String> getLog() {
    // return RobotAccess.getRobot().getLoggerList();
    // }

    // @PutMapping("/robot/log")
    // public void addLog(@RequestBody String log) {
    // if (log == null) {
    // RobotAccess.getRobot().addtoLoggerList("Bad Request");
    // throw new ResponseStatusException(HttpStatus.BAD_REQUEST);
    // }
    // RobotAccess.getRobot().addtoLoggerList(log);
    // }

    // @GetMapping("/robot/image")
    // public String getImage() {
    // return "image";
    // }

    // @PutMapping("/robot/image")
    // public void setImage(@RequestBody String image) {
    // if (image == null)
    // throw new ResponseStatusException(HttpStatus.BAD_REQUEST);
    // RobotAccess.getRobot().setImage(image);
    // }
}
