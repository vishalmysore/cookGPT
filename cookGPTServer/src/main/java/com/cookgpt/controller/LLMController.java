package com.cookgpt.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class LLMController {

    @GetMapping("/llmName")
    public ResponseEntity<String> llmName() {
        String s = "gptcook";
        return  ResponseEntity.ok(s);
    }
    @GetMapping("/finetune")
    public ResponseEntity<String> finetune() {
        String s = "gptcook";
        return  ResponseEntity.ok(s);
    }

    @GetMapping("/changeLLM")
    public ResponseEntity<String> changeLLM() {
        String s = "gptcook";
        return  ResponseEntity.ok(s);
    }
}
