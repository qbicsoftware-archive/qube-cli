package life.qbic.gui;

import life.qbic.javafx.QBiCApplication;

import javafx.stage.Stage;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

/**
 * Implementation of {{ cookiecutter.project_name }}. Its command-line arguments are contained in instances of {@link {{ cookiecutter.main_class_prefix }}Command}.
 */
public class {{ cookiecutter.main_class_prefix }}Application extends QBiCApplication<{{ cookiecutter.main_class_prefix }}Command> {

    private static final Logger LOG = LogManager.getLogger({{ cookiecutter.main_class_prefix }}Application.class);

    @Override
    public void start(final Stage stage) throws Exception {
        // TODO: do the JavaFX thing
    }
}
