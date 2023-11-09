package com.AMRCapstone.AMRCapstone.model;

import com.AMRCapstone.AMRCapstone.Codes;
import com.AMRCapstone.AMRCapstone.access.QRAccess;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;

import jakarta.validation.constraints.NotEmpty;

@JsonInclude(JsonInclude.Include.ALWAYS)
public class QR {
    @NotEmpty
    private String name;
    @NotEmpty
    private String status;

    @NotEmpty
    private String code;

    private float x_pos;
    private float y_pos;

    private static final String typeBreaker = "#";

    public QR() {

    }

    public QR(/* String name, */String status, String code, float x_pos, float y_pos) {
        if ((status != Codes.QRActive && status != Codes.QRLost) || code == null)
            return;
        this.name = "QR_Code_" + x_pos + "_" + y_pos;
        this.status = status;
        this.code = code;
        this.x_pos = x_pos;
        this.y_pos = y_pos;
    }

    @JsonProperty("name")
    public String getName() {
        return name;
    }

    public String getFileName() {
        return name + ".jpg";
    }

    @JsonProperty("status")
    public String getStatus() {
        return status;
    }

    @JsonProperty("code")
    public String getCode() {
        return code;
    }

    @JsonProperty("x_pos")
    public float getX_pos() {
        return x_pos;
    }

    @JsonProperty("y_pos")
    public float getY_pos() {
        return y_pos;
    }

    public void setStatus(String statusUpdate) {
        if (!this.status.equals(statusUpdate)) {
            this.status = statusUpdate;
            /* --- SHOULD BE COMMENTED OUT FOR TEST CASES --- */
            QRAccess.saveQRCodes();
        }

    }

    @Override
    public String toString() {
        /* QR_Code_1_1#00000000010000010#1#1#Active */

        return name + typeBreaker + code + typeBreaker + (int) (x_pos) + typeBreaker + (int) (y_pos) + typeBreaker
                + status;
    }

}
