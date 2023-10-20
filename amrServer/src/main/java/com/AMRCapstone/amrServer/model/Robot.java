package com.AMRCapstone.amrServer.model;

import java.util.ArrayList;
// import java.util.UUID;

// import org.hibernate.validator.internal.util.logging.Log_.logger;

// import org.springframework.lang.Nullable;

import jakarta.validation.constraints.NotEmpty;
import jakarta.validation.constraints.NotNull;

@NotNull
public class Robot {

    // robot's id
    private int id;

    // status of robot.. i.e. "Active" / "Inactive" / "Connection Lost"
    @NotEmpty
    private String status;

    // a general overview of what the robot is currently doing.. i.e. "heading to QR
    // code"
    @NotEmpty
    private String message;

    // robot's position and rotation
    private float x_pos;
    private float y_pos;
    private float rotation;

    // robot's destination
    private float x_destination;
    private float y_destination;

    // qr code that has just been scanned
    private String qrScan = null;

    // list of robot's actions
    private ArrayList<String> loggerList;

    // image or video from robot's camera
    // object type need to be changed
    @NotEmpty
    private Byte[] image = null;

    public Robot(int id, String status, String message, float x_pos, float y_pos, float rotation,
            float x_destination, float y_destination, String qrScan, ArrayList<String> logger, Byte[] image) {
        this.id = id;
        this.status = status;
        this.message = message;
        this.x_pos = x_pos;
        this.y_pos = y_pos;
        this.rotation = rotation;
        this.x_destination = x_destination;
        this.y_destination = y_destination;
        this.qrScan = qrScan;
        this.loggerList = logger;
        this.image = image;
    }

    public Robot(int id, String status, String message, float x_pos, float y_pos, float rotation) {
        this.id = id;
        this.status = status;
        this.message = message;
        this.x_pos = x_pos;
        this.y_pos = y_pos;
        this.rotation = rotation;
        this.x_destination = 0;
        this.y_destination = 0;
        this.qrScan = null;
        this.loggerList = new ArrayList<String>();
        this.image = null;
    }

    public Robot() {

    }

    public int getId() {
        return id;
    }

    public String getStatus() {
        return status;
    }

    public String getMessage() {
        return message;
    }

    public float getX_pos() {
        return x_pos;
    }

    public float getY_pos() {
        return y_pos;
    }

    public float getRotation() {
        return rotation;
    }

    public float getX_destination() {
        return x_destination;
    }

    public float getY_destination() {
        return y_destination;
    }

    public String getQrScan() {
        return qrScan;
    }

    public ArrayList<String> getLoggerList() {
        return loggerList;
    }

    public Byte[] getImage() {
        return image;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public void setX_pos(float x_pos) {
        this.x_pos = x_pos;
    }

    public void setY_pos(float y_pos) {
        this.y_pos = y_pos;
    }

    public void setRotation(float rotation) {
        this.rotation = rotation;
    }

    public void setX_destination(float x_destination) {
        this.x_destination = x_destination;
    }

    public void setY_destination(float y_destination) {
        this.y_destination = y_destination;
    }

    public void setQrScan(String qrScan) {
        this.qrScan = qrScan;
    }

    public void setLoggerList(ArrayList<String> loggerList) {
        this.loggerList = loggerList;
    }

    public void addtoLoggerList(String action) {
        if (action == null)
            return;
        this.loggerList.add(action);
    }

    public void addtoLoggerList(ArrayList<String> loggerList) {
        if (loggerList == null)
            return;
        this.loggerList.addAll(loggerList);
    }

    public void setImage(Byte[] image) {
        if (image == null)
            return;
        this.image = image;
    }

}
