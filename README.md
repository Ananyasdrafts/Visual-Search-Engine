# Image Search Engine

Welcome to the Image Search Engine! This project enables you to find visually similar images by providing an input image. Leveraging advanced image processing techniques, this search engine analyzes the visual content of images to identify similarities, making it a powerful tool for various applications such as digital asset management, content discovery, and more.

The image search engine operates through a well-defined pipeline, which includes:

1. **Defining your image descriptor**: Determine which aspects of the image are of interest, such as color, shape, or texture.
2. **Indexing your dataset**: Extract features from each image in the dataset using the defined descriptor and store them for later comparison.
3. **Defining your similarity metric**: Choose a method to compare feature vectors, such as Euclidean distance or Cosine distance.
4. **Searching**: Extract features from a query image, compare them to the indexed features using the similarity metric, and return the most relevant results.

## Repository Structure

- `ColorDescriptor.py`: Defines the image descriptor that extracts features from images based on color.
- `index.py`: Applies the image descriptor to each image in the dataset and writes the features to storage.
- `searcher.py`: Defines the similarity metric and performs the search by comparing feature vectors.
- `search.py`: Handles the process of receiving a query image, extracting its features, and returning the most relevant search results.
- `requirements.txt`: Lists all the necessary libraries and dependencies required for the project, ensuring a smooth setup and consistent environment.

### Prerequisites

- Python 3.x
- Required libraries in `requirements.txt`

### License

This project is licensed under the GNU General Public License v3.0. See the LICENSE file for more details.

### Contributing

We welcome contributions to enhance the functionality and features of this project. To contribute, please fork the repository, create a new branch, make your changes, and submit a pull request.

### Contact

For any questions or suggestions, please open an issue in this repository or contact the project maintainer at ananyag1019@gmail.com.


