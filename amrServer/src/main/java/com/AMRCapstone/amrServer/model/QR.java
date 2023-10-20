package com.AMRCapstone.amrServer.model;

import jakarta.validation.constraints.NotEmpty;

public class QR {
    @NotEmpty
    private String name;
    @NotEmpty
    private String status;
    @NotEmpty
    private String image;
    @NotEmpty
    private String code;

    private float x_pos;
    private float y_pos;

    public QR() {

    }

    public QR(String name, String status, String image, String code, float x_pos, float y_pos) {
        this.name = name;
        this.status = status;
        this.image = image;
        this.code = code;
        this.x_pos = x_pos;
        this.y_pos = y_pos;
    }

    public String getName() {
        return name;
    }

    public String getStatus() {
        return status;
    }

    public String getImage() {
        return image;
    }

    public String getCode() {
        return code;
    }

    public float getX_pos() {
        return x_pos;
    }

    public float getY_pos() {
        return y_pos;
    }

    public void setStatus(String status) {
        this.status = status;
    }

}
