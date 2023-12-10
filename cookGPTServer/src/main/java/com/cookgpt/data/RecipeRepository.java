package com.cookgpt.data;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

import java.util.List;

public interface RecipeRepository extends MongoRepository<Recipe, String> {
    List<Recipe> findAll();
    List<Recipe> findByContentsContaining(String contents);

    @Query("{$text: {$search: ?0}}")
    List<Recipe> findByTextSearch(String keyword);
}
