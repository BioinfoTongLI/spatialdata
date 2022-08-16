from typing import Callable

import numpy as np
import pytest
from anndata import AnnData

from spatialdata import SpatialData


def get_empty_sdata():
    return SpatialData()


def get_features_sdata(dim0=20):
    return SpatialData(tables={"tables": AnnData(np.ones((dim0, 10)))})


def get_regions_sdata(dim0=20):
    return SpatialData(labels={"labels": np.ones((dim0, 10))})


def get_images_sdata(dim0=20):
    return SpatialData(images={"image": np.ones((dim0, 10, 10))})


def get_points_sdata(dim0=20):
    return SpatialData(points={"points": AnnData(np.ones((dim0, 10)))})


def get_shapes_sdata(dim0=20):
    return SpatialData(shapes={"shapes": AnnData(np.ones((dim0, 10)))})


@pytest.mark.parametrize(
    "getter1", [get_empty_sdata, get_features_sdata, get_regions_sdata, get_images_sdata, get_points_sdata]
)
@pytest.mark.parametrize(
    "getter2", [get_empty_sdata, get_features_sdata, get_regions_sdata, get_images_sdata, get_points_sdata]
)
@pytest.mark.skip(reason="Not implemented")
def test_single_component_sdata(getter1: Callable, getter2: Callable):
    if getter1 == getter2:
        assert getter1() == getter2()