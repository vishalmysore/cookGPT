package com.cookgpt.data;

import lombok.*;
import org.springframework.data.mongodb.core.mapping.Document;

@Data
@ToString(includeFieldNames = true)
@NoArgsConstructor
@AllArgsConstructor
@Setter
@Getter

public class ContributeRecipe {
    String name;
    String instructions;
    String contributor;
    String contents;
}
