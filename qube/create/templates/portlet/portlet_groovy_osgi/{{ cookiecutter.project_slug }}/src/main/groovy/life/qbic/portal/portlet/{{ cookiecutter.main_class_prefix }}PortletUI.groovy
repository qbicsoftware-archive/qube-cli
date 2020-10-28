package life.qbic.portal.portlet

import com.liferay.portal.kernel.log.Log
import com.liferay.portal.kernel.log.LogFactoryUtil

import com.vaadin.annotations.Theme
import com.vaadin.icons.VaadinIcons
import com.vaadin.server.VaadinRequest
import com.vaadin.server.VaadinService
import com.vaadin.shared.ui.ContentMode
import com.vaadin.ui.*
import com.vaadin.ui.themes.ValoTheme


import org.osgi.framework.Bundle
import org.osgi.framework.FrameworkUtil
import org.osgi.service.component.annotations.Component
import org.osgi.service.component.annotations.ServiceScope


@Theme("mytheme")
@SuppressWarnings("serial")
//@Widgetset("life.qbic.portal.portlet.AppWidgetSet")
@Component(
    service = UI.class,
    property = {
        "com.liferay.portlet.display-category=category.sample",  // Widget category
        "javax.portlet.name=MyVaadinPortlet",                    // Unique portlet name in Liferay
        "javax.portlet.display-name=OSGi Portlet",               // Portlet display name
        "javax.portlet.security-role-ref=power-user,user",       // Default user roles
        "com.vaadin.osgi.liferay.portlet-ui=true",
        "service.ranking:Integer=1000"},              // Is Vaadin UI?
    scope = ServiceScope.PROTOTYPE)  // New instance created for each distinct request. Mandatory.
class {{ cookiecutter.main_class_prefix }}PortletUI extends UI {

    private static final Log log = LogFactoryUtil.getLog({{ cookiecutter.main_class_prefix }}PortletUI.class)

    // Get Bundle metadata at runtime
    //private static final Bundle bundle = FrameworkUtil.getBundle(MyPortletUI.class);
    // private static final String portletName    = bundle.getHeaders().get("Bundle-Name");
    //private static final String portletVersion = bundle.getVersion().toString();
    //private static final String portletRepoURL = bundle.getHeaders().get("Bundle-DocURL");


    @Override
    protected void init(VaadinRequest request) {
        setStyleName("app-bg")  // White portlet background --> mytheme.scss

        // Get user of current request. Is null if user is not logged in
        String user = VaadinService.getCurrentRequest().getRemoteUser()
        log.debug("Page requested from: " + user)

        // Create layout with error message if user is not logged in
        if (user == null) {
            setContent(buildNotLoggedInLayout())
            return;
        }

        final Layout layout = getPortletContent()
        addPortletInfo(layout)

        setContent(layout)
    }

    private Layout getPortletContent() {
        final VerticalLayout textArea = new VerticalLayout();
        textArea.setSpacing(true);
        textArea.setMargin(true);

        // Button which on click communicates with the example osgi library
        final Button random = new Button("Get Random String")
        random.addClickListener( event -> {
        String tmp = "" //LibraryExample.getRandomString();""
        textArea.addComponent(
            new Label("<p>"+tmp.replace("\n", "<br/>")+"</p>", ContentMode.HTML) )
        })

        // Button to clean the text area if it gets too crowded
        final Button reset = new Button(VaadinIcons.TRASH)
        reset.setStyleName(ValoTheme.BUTTON_BORDERLESS)
        reset.setDescription("Empty Text Area.")
        reset.addClickListener( event -> textArea.removeAllComponents() )

        final HorizontalLayout buttonRow = new HorizontalLayout()
        buttonRow.setSpacing(true)
        buttonRow.addComponents(random, reset)

        final VerticalLayout layout = new VerticalLayout()
        layout.setSpacing(true)
        layout.addComponents(buttonRow, textArea)

        return layout
    }

    private void addPortletInfo(final Layout layout) {
        String info = ""; //String.format("%s %s (<a href=\"%s\">%s</a>)",
        //portletName, portletVersion, portletRepoURL, portletRepoURL);

        final Label portletInfoLabel = new Label(info, ContentMode.HTML)
        portletInfoLabel.addStyleName("portlet-footer")
        portletInfoLabel.setId("qbic-portlet-info-label")

        layout.addComponent(portletInfoLabel)
        ((VerticalLayout) layout).setComponentAlignment(portletInfoLabel, Alignment.MIDDLE_RIGHT)
    }


    /**
     * Creates a layout with just an error message that the user should log in.
     *
     * @return Layout containing error message
     */
    public static Layout buildNotLoggedInLayout() {
        Label error = new Label("You have to be logged in to use this portlet.", ContentMode.HTML)
        error.addStyleNames("bigger", "redder")

        VerticalLayout loggedOut = new VerticalLayout()
        loggedOut.setWidth("100%")  // setSizeFull() does not work with setContent() in UI ...
        loggedOut.setMargin(true)
        loggedOut.setSpacing(true)
        loggedOut.addComponent(error)
        loggedOut.setComponentAlignment( error, Alignment.MIDDLE_CENTER )

        return loggedOut
    }
}
