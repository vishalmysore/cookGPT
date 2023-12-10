package com.cookgpt.data;

import lombok.*;
import org.springframework.data.mongodb.core.index.TextIndexed;
import org.springframework.data.mongodb.core.mapping.Document;
import org.springframework.data.annotation.Id;
@Data
@ToString(includeFieldNames = true)
@NoArgsConstructor
@AllArgsConstructor
@Setter
@Getter
@RequiredArgsConstructor
@Document(collection = "recipes")
public class Recipe {
    @NonNull
    @Id
    private String id;
    @NonNull
    private String name;
   private String instructions;
   @TextIndexed
   private String contents;
   private String contributor;
   int rating;

}
