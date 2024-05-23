#!/usr/bin/node

// Import the request module to make HTTP requests
// Get the movie ID from command line arguments
// Construct the URL for the movie API endpoint
const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Check if movieId is provided
if (!movieId) {
  // Print error message if no movie ID is provided
  // Exit the script with an error code
  console.error('Please provide a Movie ID');
  process.exit(1);
}

// Make an HTTP request to the movie API endpoint
request(apiUrl, async (error, response, body) => {
  // Handle any errors during the request
  if (error) {
    // Print error message
    // Exit the script with an error code
    console.error('Error fetching movie data:', error);
    process.exit(1);
  }

  // Check if the response status is not 200 (OK)
  if (response.statusCode !== 200) {
    // Print status code error
    // Exit the script with an error code
    console.error('Failed to fetch movie data. Status code:', response.statusCode);
    process.exit(1);
  }

  // Parse the response body as JSON to get the movie data
  // Get the list of character URLs from the movie data
  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  // Check if there are no characters in the movie
  if (!characters || characters.length === 0) {
    // Print error message if no characters are found
    // Exit the script with an error code
    console.error('No characters found for this movie.');
    process.exit(1);
  }

  // Iterate over the list of character URLs
  for (const characterUrl of characters) {
    // Create a new promise to handle asynchronous requests in sequence
    await new Promise((resolve, reject) => {
      // Make an HTTP request to each character URL
      request(characterUrl, (error, response, body) => {
        // Handle any errors during the request
        if (error) {
          // Print error message
          // Reject the promise with the error
          console.error('Error fetching character data:', error);
          reject(error);
          return;
        }

        // Check if the response status is not 200 (OK)
        if (response.statusCode !== 200) {
          // Print status code error
          // Reject the promise with a new error
          console.error('Failed to fetch character data. Status code:', response.statusCode);
          reject(new Error(`Status code: ${response.statusCode}`));
          return;
        }

        // Parse the response body as JSON to get the character data
        const characterData = JSON.parse(body);
        // Print the character name
        console.log(characterData.name);
        // Resolve the promise to proceed with the next character
        resolve();
      });
    });
  }
});
