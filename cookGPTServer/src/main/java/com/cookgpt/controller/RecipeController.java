package com.cookgpt.controller;

import com.cookgpt.data.ContributeRecipe;
import com.cookgpt.data.Rating;
import com.cookgpt.data.Recipe;
import com.cookgpt.service.RecipeService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController

public class RecipeController {

    private final RecipeService recipeService;

    @Autowired
    public RecipeController(RecipeService recipeService) {
        this.recipeService = recipeService;
    }

    @GetMapping("/getAllRecipes")
    public  ResponseEntity<List<Recipe>> getAllRecipes() {
        return ResponseEntity.ok(recipeService.getAllRecipes());
    }
    @PostMapping("/saveRecipe")
    public Recipe saveRecipe(@RequestBody Recipe recipe) {
        return recipeService.saveRecipe(recipe);
    }
    @PostMapping("/addRecipe")
    public Recipe contribteRecipe(@RequestBody ContributeRecipe recipe) {
        Recipe recipeNew = new Recipe();
        recipeNew.setName(recipe.getName());
        recipeNew.setInstructions(recipe.getInstructions());
        recipeNew.setContributor(recipe.getContributor());
        recipeNew.setContents(recipe.getContents());
        return recipeService.saveRecipe(recipeNew);
    }

    @PostMapping("/rateRecipe")
    public Recipe rateRecipe(@RequestBody Rating recipe) {

        return null;
    }

    @GetMapping("/sayHello")
    public ResponseEntity<String> sayHello() {
        String s = "Hello";
        return  ResponseEntity.ok(s);
    }
    @GetMapping("/search/{keyword}")
    public List<Recipe> findRecipesByKeyword(@PathVariable String keyword) {
        return recipeService.findRecipesByKeyword(keyword);
    }

    @GetMapping("/getAllVegetarianRecipes")
    public  ResponseEntity<List<Recipe>> getAllVegetarianRecipe() {
        return ResponseEntity.ok(recipeService.getAllRecipes());
    }

    @GetMapping("/getAllEggRecipes")
    public  ResponseEntity<List<Recipe>> getAllEggRecipe() {
        return ResponseEntity.ok(recipeService.getAllRecipes());
    }

    @GetMapping("/getAllChickenRecipes")
    public  ResponseEntity<List<Recipe>> getAllChickenRecipes() {
        return ResponseEntity.ok(recipeService.getAllRecipes());
    }

    @GetMapping("/getAllJainMeals")
    public  ResponseEntity<List<Recipe>> getAllJainMeals() {
        return ResponseEntity.ok(recipeService.getAllRecipes());
    }

    @GetMapping("/getAllRiceItems")
    public  ResponseEntity<List<Recipe>> getAllRiceItems() {
        return ResponseEntity.ok(recipeService.getAllRecipes());
    }

    @GetMapping("/getSouthIndianItems")
    public  ResponseEntity<List<Recipe>> getSouthIndianItems() {
        return ResponseEntity.ok(recipeService.getAllRecipes());
    }

    @GetMapping("/getPunjabiFoodIndianItems")
    public  ResponseEntity<List<Recipe>> getPunjabiFoodIndianItems() {
        return ResponseEntity.ok(recipeService.getAllRecipes());
    }
    @GetMapping("/getBreakFastItems")
    public  ResponseEntity<List<Recipe>> getBreakFastItems() {
        return ResponseEntity.ok(recipeService.getAllRecipes());
    }

    @GetMapping("/getSweetDishes")
    public  ResponseEntity<List<Recipe>> getSweetDishes() {
        return ResponseEntity.ok(recipeService.getAllRecipes());
    }

    @GetMapping("/getDiwaliItems")
    public  ResponseEntity<List<Recipe>> getDiwaliItems() {
        return ResponseEntity.ok(recipeService.getAllRecipes());
    }
    @GetMapping("/getFastingDishes")
    public  ResponseEntity<List<Recipe>> getFastingDishes() {
        return ResponseEntity.ok(recipeService.getAllRecipes());
    }

    @GetMapping("/getVegProtienItems")
    public  ResponseEntity<List<Recipe>> getVegProtienItems() {
        return ResponseEntity.ok(recipeService.getAllRecipes());
    }

}