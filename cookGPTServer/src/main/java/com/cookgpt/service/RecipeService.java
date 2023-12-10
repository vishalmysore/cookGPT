package com.cookgpt.service;

import com.cookgpt.data.Recipe;

import java.util.List;

public interface RecipeService {
    List<Recipe> getAllRecipes();
    Recipe saveRecipe(Recipe recipe);
    List<Recipe> findRecipesByKeyword(String keyword);
}
