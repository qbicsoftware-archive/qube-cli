package life.qbic.portal.portlet

import com.vaadin.annotations.Theme
import com.vaadin.annotations.Widgetset
import com.vaadin.server.VaadinRequest
import com.vaadin.ui.Button
import com.vaadin.ui.Label
import com.vaadin.ui.Layout
import com.vaadin.ui.TextField
import com.vaadin.ui.VerticalLayout
import groovy.transform.CompileStatic
import groovy.util.logging.Log4j2

/**
 * Entry point for portlet {{ cookiecutter.project_slug }}. This class derives from {@link QBiCPortletUI}, which is found in the {@code portal-utils-lib} library.
 *
 * @see <a href=https://github.com/qbicsoftware/portal-utils-lib>portal-utils-lib</a>
 */
@Theme("mytheme")
@SuppressWarnings("serial")
@Log4j2
@CompileStatic
class ExampleApp extends QBiCPortletUI {

    @Override
    protected Layout getPortletContent(final VaadinRequest request) {
        log.info"Generating content for {}"

        // TODO: generate content for your portlet
        //       this method returns any non-null layout to avoid a NullPointerException later on
        def layout = new VerticalLayout()

        def name = new TextField()
        name.setCaption("Type your name here:")

        Button button = new Button("Click Me please Sven!")
        button.addClickListener({ e ->
        layout.addComponent(new Label("Thanks " + name.getValue() + ", it works!"))
        })
        layout.addComponents(name, button)
        return layout
    }
}
