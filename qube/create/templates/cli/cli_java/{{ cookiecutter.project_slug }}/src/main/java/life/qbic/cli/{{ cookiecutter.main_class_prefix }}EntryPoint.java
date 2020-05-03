package life.qbic.cli;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

/**
 * Entry point for the {{ cookiecutter.project_name }} application.
 *
 * The purpose of this class is to act as a bridge between the command line and the <i>real</i> implementation of a tool by using a {@link ToolExecutor}.
 */
public class {{ cookiecutter.main_class_prefix }}EntryPoint {

    private static final Logger LOG = LogManager.getLogger({{ cookiecutter.main_class_prefix }}EntryPoint.class);

    /**
     * Main method.
     *
     * @param args the command-line arguments.
     */
    public static void main(final String[] args) {
        LOG.debug("Starting {{ cookiecutter.main_class_prefix }} tool");
        final ToolExecutor executor = new ToolExecutor();
        executor.invoke({{ cookiecutter.main_class_prefix }}Tool.class, {{ cookiecutter.main_class_prefix }}Command.class, args);
    }
}
