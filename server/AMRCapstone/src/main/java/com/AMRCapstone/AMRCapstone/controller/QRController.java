package com.AMRCapstone.AMRCapstone.controller;

import java.util.Collection;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.server.ResponseStatusException;

import com.AMRCapstone.AMRCapstone.access.QRAccess;
import com.AMRCapstone.AMRCapstone.model.QR;
import com.AMRCapstone.AMRCapstone.service.QRService;

import jakarta.validation.Valid;

@RestController
public class QRController {
    // private Map<String, QR> QRDB = new HashMap<>() {
    // {
    // put("QR_Code_2-5", new QR("QR_Code_2_5", "Active", "image", "342wfer89", 2,
    // 5));
    // put("QR_Code_2-4", new QR("QR_Code_2_4", "Active", "image", "879g2f3", 2,
    // 4));
    // put("QR_Code_1-5", new QR("QR_Code_1_5", "Missing", "image", "f2g34798", 1,
    // 5));
    // }
    // };

    private final QRService QrService;

    public QRController(QRService QrService) {
        this.QrService = QrService;
    }

    @GetMapping("/qr")
    public Collection<QR> getQRCodes() {
        return QRAccess.getQRs().values();
    }

    @GetMapping("/qr/{name}")
    public QR getQR(@PathVariable String name) throws Exception {
        QR qr = QRAccess.getQRs().get(name);
        if (qr == null)
            throw new ResponseStatusException(HttpStatus.NOT_FOUND);
        return qr;
    }

    @GetMapping("/qr/{name}/name")
    public String getName(@PathVariable String name) throws Exception {
        QR qr = QRAccess.getQRs().get(name);
        if (qr == null)
            throw new ResponseStatusException(HttpStatus.NOT_FOUND);
        return qr.getName();
    }

    @GetMapping("/qr/{name}/status")
    public String getStatus(@PathVariable String name) throws Exception {
        QR qr = QRAccess.getQRs().get(name);
        if (qr == null)
            throw new ResponseStatusException(HttpStatus.NOT_FOUND);
        return qr.getStatus();
    }

    @PutMapping("/qr/{name}/status")
    public void updateStatus(@PathVariable String name, @RequestBody @Valid String Status) throws Exception {
        QrService.updateStatus(name, Status);
    }

    // @GetMapping("/qr/{name}/image")
    // public String getImage(@PathVariable String name) throws Exception {
    // QR qr = QRAccess.getQRs().get(name);
    // if (qr == null)
    // throw new ResponseStatusException(HttpStatus.NOT_FOUND);
    // return qr.getImage();
    // }

    // @GetMapping("/qr/{name}/code")
    // public String getQRCode(@PathVariable String name) throws Exception {
    // QR qr = QRAccess.getQRs().get(name);
    // if (qr == null)
    // throw new ResponseStatusException(HttpStatus.NOT_FOUND);
    // return qr.getCode();
    // }

    // @GetMapping("/qr/{name}/position")
    // public float[] getPosition(@PathVariable String name) throws Exception {
    // QR qr = QRAccess.getQRs().get(name);
    // if (qr == null)
    // throw new ResponseStatusException(HttpStatus.NOT_FOUND);
    // float[] position = {
    // qr.getX_pos(),
    // qr.getY_pos()
    // };
    // return position;
    // }
}
