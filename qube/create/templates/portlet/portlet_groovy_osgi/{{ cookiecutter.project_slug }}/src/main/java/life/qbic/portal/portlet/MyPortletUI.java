package life.qbic.portal.portlet;

import com.liferay.portal.kernel.log.Log;
import com.liferay.portal.kernel.log.LogFactoryUtil;

import com.vaadin.annotations.Theme;
import com.vaadin.icons.VaadinIcons;
import com.vaadin.server.VaadinRequest;
import com.vaadin.server.VaadinService;
import com.vaadin.shared.ui.ContentMode;
import com.vaadin.ui.*;
import com.vaadin.ui.themes.ValoTheme;

import life.qbic.example.Car;
import life.qbic.example.Garage;
import org.osgi.service.component.annotations.Component;
import org.osgi.service.component.annotations.ServiceScope;


@Theme("mytheme")
@SuppressWarnings("serial")
@Component(
        service = UI.class,
        property = {
        "com.liferay.portlet.display-category=category.sample",  // Widget category
        "javax.portlet.name=example-osgi-portlet-1.2.0",         // Unique portlet name in Liferay
        "javax.portlet.display-name=OSGi Portlet",               // Portlet display name
        "javax.portlet.security-role-ref=power-user,user",       // Default user roles
        "com.vaadin.osgi.liferay.portlet-ui=true" },             // Is Vaadin UI?
        scope = ServiceScope.PROTOTYPE)  // New instance created for each distinct request. Mandatory.
public class MyPortletUI extends UI {
    private static final Log log = LogFactoryUtil.getLog(MyPortletUI.class);

    private static final PortletInformation info = new PortletInformation();

    @Override
    protected void init(VaadinRequest request) {
        setStyleName("app-bg");  // White portlet background --> mytheme.scss

        // Get user of current request. Is null if user is not logged in
        String user = VaadinService.getCurrentRequest().getRemoteUser();
        log.debug("Page requested from: " + user);

        final Layout layout = getPortletContent();
        addPortletInfo(layout);

        setContent(layout);

        // Validate Groovy compilation works
        GroovyCar.start();

        // Validate external OSGi bundle works
        Car car = Garage.requestCar();
        car.startEngine();
    }

    private Layout getPortletContent() {
        final VerticalLayout textArea = new VerticalLayout();
        textArea.setSpacing(true);
        textArea.setMargin(true);

        // Button which on click communicates with the example osgi library
        final Button random = new Button("Get Random String");
        random.addClickListener( event -> {
            String tmp = "Fixed String!";
            textArea.addComponent(
                    new Label("<p>"+tmp.replace("\n", "<br/>")+"</p>", ContentMode.HTML) );
        });

        // Button to clean the text area if it gets too crowded
        final Button reset = new Button(VaadinIcons.TRASH);
        reset.setStyleName(ValoTheme.BUTTON_BORDERLESS);
        reset.setDescription("Empty Text Area.");
        reset.addClickListener( event -> textArea.removeAllComponents() );

        final HorizontalLayout buttonRow = new HorizontalLayout();
        buttonRow.setSpacing(true);
        buttonRow.addComponents(random, reset);

        final VerticalLayout layout = new VerticalLayout();
        layout.setSpacing(true);
        layout.addComponents(buttonRow, textArea);

        return layout;
    }

    private void addPortletInfo(final Layout layout) {
        String info = getPortletInfoAsHTML();

        final Label portletInfoLabel = new Label(info, ContentMode.HTML);
        portletInfoLabel.addStyleName("portlet-footer");
        portletInfoLabel.setId("qbic-portlet-info-label");

        layout.addComponent(portletInfoLabel);
        ((VerticalLayout) layout).setComponentAlignment(portletInfoLabel, Alignment.MIDDLE_RIGHT);
    }

    private static String getPortletInfoAsHTML() {
        return String.format("%s %s (<a href=\"%s\">%s</a>)",
            info.getPortletName(),
            info.getPortletVersion(),
            info.getPortletRepoURL(),
            info.getPortletRepoURL());
    }
}
