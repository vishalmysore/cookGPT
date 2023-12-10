package com.cookgpt.data;

import lombok.*;

@Data
@ToString(includeFieldNames = true)
@NoArgsConstructor
@AllArgsConstructor
@Setter
@Getter
public class Rating {
    String id;
    int rating;
    String receipeId;
    String contributorId;
}
