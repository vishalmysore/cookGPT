package com.cookgpt.service;

import com.cookgpt.data.Recipe;
import com.cookgpt.data.RecipeRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class RecipeServiceImpl implements RecipeService {
    private final RecipeRepository recipeRepository;

    @Autowired
    public RecipeServiceImpl(RecipeRepository recipeRepository) {
        this.recipeRepository = recipeRepository;
    }

    public Recipe saveRecipe(Recipe recipe) {
        return recipeRepository.save(recipe);
    }
    @Override
    public List<Recipe> getAllRecipes() {

        return recipeRepository.findAll();
    }
    @Override
    public List<Recipe> findRecipesByKeyword(String keyword) {
        // Use either method based on your preference
        // return recipeRepository.findByKeywordsContaining(keyword);
        return recipeRepository.findByTextSearch(keyword);
    }
}
