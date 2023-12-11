package com.cookgpt.data;

import lombok.*;

@Data
@ToString(includeFieldNames = true)
@NoArgsConstructor
@AllArgsConstructor
@Setter
@Getter
@RequiredArgsConstructor
public class NutritionalValue {
    String id;
    Long protein;
    Long carbs;
    Long sodium;
    Long potassium;

}
