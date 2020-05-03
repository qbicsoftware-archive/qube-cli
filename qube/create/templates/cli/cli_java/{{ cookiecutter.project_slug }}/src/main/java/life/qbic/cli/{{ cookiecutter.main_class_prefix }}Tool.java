package life.qbic.cli;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

/**
 * Implementation of {{ cookiecutter.project_name }}. Its command-line arguments are contained in instances of {@link {{ cookiecutter.main_class_prefix }}Command}.
 */
public class {{ cookiecutter.main_class_prefix }}Tool extends QBiCTool<{{ cookiecutter.main_class_prefix }}Command> {

    private static final Logger LOG = LogManager.getLogger({{ cookiecutter.main_class_prefix }}Tool.class);

    /**
     * Constructor.
     *
     * @param command an object that represents the parsed command-line arguments.
     */
    public {{ cookiecutter.main_class_prefix }}Tool(final {{ cookiecutter.main_class_prefix }}Command command) {
        super(command);
    }

    @Override
    public void execute() {
        // get the parsed command-line arguments
        final {{ cookiecutter.main_class_prefix }}Command command = super.getCommand();

        // TODO: do something useful with the obtained command.
        //

    }

    // TODO: override the shutdown() method if you are implementing a daemon and want to take advantage of a shutdown hook for clean-up tasks
}
