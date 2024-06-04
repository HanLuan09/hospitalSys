package com.devteria.gateway.repository;

import com.devteria.gateway.dto.response.IntrospectResponse;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.service.annotation.PostExchange;
import reactor.core.publisher.Mono;

public interface IdentityClient {
    @PostExchange(url = "/valid/", contentType = MediaType.APPLICATION_JSON_VALUE)
    Mono<IntrospectResponse> introspect(@RequestHeader("Authorization") String token);
}
