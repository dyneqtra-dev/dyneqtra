import importlib

from pydantic import BaseModel


class NodeTypeSchema(BaseModel):
    node_type_name: str
    class_name: str
    module: str

    @property
    def node_class(self):
        module = importlib.import_module(name=f"{self.module}", package="app")
        return getattr(module, self.class_name)

    @property
    def input_model(self):
        return self.node_class.input_model

    @property
    def display_name(self) -> str:
        """Get the display name for the node type, falling back to class name if not set."""
        node_class = self.node_class
        return node_class.display_name or node_class.__name__
    
    @property
    def logo(self) -> str:
        """Get the logo for the node type, falling back to None if not set."""
        node_class = self.node_class
        return node_class.logo or ""

    @property
    def config_title(self) -> str:
        """Get the title to use for the config, using display name."""
        return self.display_name


class MinimumNodeConfigSchema(BaseModel):
    node_type: NodeTypeSchema
