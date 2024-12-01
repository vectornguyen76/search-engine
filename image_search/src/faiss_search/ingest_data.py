import os

import faiss
import numpy as np
from config import settings
from src.utils import LOGGER, time_profiling


class FaissIngest:
    """
    A class for ingesting data into a Faiss index.

    Attributes:
        image_features (numpy.ndarray): Array of features to be indexed.
    """

    def __init__(self):
        """
        Initializes a FaissIngest instance and loads array features from a file.
        """
        # Load array features from the specified file
        self.image_features = np.load(settings.FEATURES_PATH, allow_pickle=True)

    def check_index_exists(self):
        return os.path.exists(settings.INDEX_PATH)

    @time_profiling
    def create_index(self):
        """
        Creates a Faiss index, adds array features to it, and saves the index to disk.

        Returns:
            None
        """
        # Create an index with FAISS using L2 distance metric
        index_faiss = faiss.IndexFlatL2(settings.DIMENSIONS)

        # Add the array features to the Faiss index
        index_faiss.add(self.image_features["image_features"])

        # Save the index to disk
        faiss.write_index(index_faiss, settings.INDEX_PATH)

        # Print a success message
        LOGGER.info("Faiss index created successfully!")
