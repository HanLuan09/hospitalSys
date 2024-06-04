package com.devteria.gateway.service;

import com.devteria.gateway.dto.response.IntrospectResponse;
import com.devteria.gateway.repository.IdentityClient;
import lombok.AccessLevel;
import lombok.RequiredArgsConstructor;
import lombok.experimental.FieldDefaults;
import org.springframework.stereotype.Service;
import reactor.core.publisher.Mono;

@Service
@RequiredArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE, makeFinal = true)
public class IdentityService {
	
    IdentityClient identityClient;


    public Mono<IntrospectResponse> introspect(String token){
        String bearerToken = "Bearer " + token;
        return identityClient.introspect(bearerToken);
    }
}
