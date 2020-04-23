package life.qbic.service;

import life.qbic.cli.QBiCTool;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

/**
 * Implementation of {{ cookiecutter.project_name }}. Its command-line arguments are contained in instances of {@link {{ cookiecutter.main_class_prefix }}Command}.
 */
public class {{ cookiecutter.main_class_prefix }}Service extends QBiCTool<{{ cookiecutter.main_class_prefix }}Command> {

    private static final Logger LOG = LogManager.getLogger({{ cookiecutter.main_class_prefix }}Service.class);

    /**
     * Constructor.
     *
     * @param command an object that represents the parsed command-line arguments.
     */
    public {{ cookiecutter.main_class_prefix }}Service(final {{ cookiecutter.main_class_prefix }}Command command) {
        super(command);
    }

    @Override
    public void execute() {
        // get the parsed command-line arguments
        final {{ cookiecutter.main_class_prefix }}Command command = super.getCommand();

        // TODO: do something useful with the obtained command.
        //
    }

    @Override
    public void shutdown() {
        // TODO: perform clean-up tasks
        // Important: do not call System.exit. This method is executed by a "shutdown hook thread"
        //            See: https://docs.oracle.com/javase/8/docs/api/java/lang/Runtime.html#exit-int-
    }
}
