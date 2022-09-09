import unittest

from super_gradients.training import models

import super_gradients

from super_gradients import Trainer
from super_gradients.training.datasets.dataset_interfaces import LibraryDatasetInterface
from super_gradients.training.dataloaders.dataloader_factory import (
    cifar10_train,
    cifar10_val,
    cifar100_train,
    cifar100_val,
)


class TestCifarTrainer(unittest.TestCase):
    def test_train_cifar10(self):
        super_gradients.init_trainer()
        trainer = Trainer("test", model_checkpoints_location="local")
        cifar_10_dataset_interface = LibraryDatasetInterface(name="cifar10")
        trainer.connect_dataset_interface(cifar_10_dataset_interface)
        model = models.get("resnet18_cifar", arch_params={"num_classes": 10})
        trainer.train(
            model=model,
            training_params={
                "max_epochs": 1,
                "initial_lr": 0.1,
                "loss": "cross_entropy",
                "train_metrics_list": ["Accuracy"],
                "valid_metrics_list": ["Accuracy"],
                "metric_to_watch": "Accuracy",
            },
        )

    def test_train_cifar10_dataloader(self):
        super_gradients.init_trainer()
        trainer = Trainer("test", model_checkpoints_location="local")
        cifar10_train_dl, cifar10_val_dl = cifar10_train(), cifar10_val()
        model = models.get("resnet18_cifar", arch_params={"num_classes": 10})
        trainer.train(
            model=model,
            training_params={
                "max_epochs": 1,
                "initial_lr": 0.1,
                "loss": "cross_entropy",
                "train_metrics_list": ["Accuracy"],
                "valid_metrics_list": ["Accuracy"],
                "metric_to_watch": "Accuracy",
            },
            train_loader=cifar10_train_dl,
            valid_loader=cifar10_val_dl,
        )

    def test_train_cifar100(self):
        super_gradients.init_trainer()
        trainer = Trainer("test", model_checkpoints_location="local")
        cifar_10_dataset_interface = LibraryDatasetInterface(name="cifar100")
        trainer.connect_dataset_interface(cifar_10_dataset_interface)
        model = models.get("resnet18_cifar", arch_params={"num_classes": 100})
        trainer.train(
            model=model,
            training_params={
                "max_epochs": 1,
                "initial_lr": 0.1,
                "loss": "cross_entropy",
                "train_metrics_list": ["Accuracy"],
                "valid_metrics_list": ["Accuracy"],
                "metric_to_watch": "Accuracy",
            },
        )

    def test_train_cifar100_dataloader(self):
        super_gradients.init_trainer()
        trainer = Trainer("test", model_checkpoints_location="local")
        cifar100_train_dl, cifar100_val_dl = cifar100_train(), cifar100_val()
        model = models.get("resnet18_cifar", arch_params={"num_classes": 100})
        trainer.train(
            model=model,
            training_params={
                "max_epochs": 1,
                "initial_lr": 0.1,
                "loss": "cross_entropy",
                "train_metrics_list": ["Accuracy"],
                "valid_metrics_list": ["Accuracy"],
                "metric_to_watch": "Accuracy",
            },
            train_loader=cifar100_train_dl,
            valid_loader=cifar100_val_dl,
        )


if __name__ == "__main__":
    unittest.main()